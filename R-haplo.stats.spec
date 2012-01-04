%global packname  haplo.stats
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.4
Release:          1%{?dist}
Summary:          Statistical Analysis of Haplotypes with Traits and Covariates when Linkage Phase is Ambiguous

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A suite of S-PLUS/R routines for the analysis of indirectly measured
haplotypes. The statistical methods assume that all subjects are unrelated
and that haplotypes are ambiguous (due to unknown linkage phase of the
genetic markers). The main functions are: haplo.em, haplo.glm,
haplo.score, haplo.power, and seqhap. Copyright: 2003 Mayo Foundation for
Medical Education and Research.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/haplo.stats/html
%doc %{rlibdir}/haplo.stats/doc
%doc %{rlibdir}/haplo.stats/NEWS
%doc %{rlibdir}/haplo.stats/DESCRIPTION
%{rlibdir}/haplo.stats/libs
%{rlibdir}/haplo.stats/demo
%{rlibdir}/haplo.stats/Meta
%{rlibdir}/haplo.stats/LICENSE
%{rlibdir}/haplo.stats/NAMESPACE
%{rlibdir}/haplo.stats/R
%{rlibdir}/haplo.stats/help
%{rlibdir}/haplo.stats/data
%{rlibdir}/haplo.stats/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.4-1
- initial package for Fedora