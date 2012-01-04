%global packname  mediation
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.1.2
Release:          1%{?dist}
Summary:          R Package for Causal Mediation Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-Matrix 

BuildRequires:    R-devel tex(latex) R-MASS R-Matrix 

%description
mediation is a publicly available R package that allows both parametric
and nonparametric causal mediation analysis. It implements the methods and
suggestions in Imai, Keele, and Yamamoto (2010) and Imai, Keele, Tingley
(2010).  In addition to the estimation of causal mediation effects, the
software also allows researchers to conduct sensitivity analysis for
certain parametric models.

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
%doc %{rlibdir}/mediation/doc
%doc %{rlibdir}/mediation/CITATION
%doc %{rlibdir}/mediation/html
%doc %{rlibdir}/mediation/DESCRIPTION
%{rlibdir}/mediation/help
%{rlibdir}/mediation/INDEX
%{rlibdir}/mediation/data
%{rlibdir}/mediation/demo
%{rlibdir}/mediation/Meta
%{rlibdir}/mediation/NAMESPACE
%{rlibdir}/mediation/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.1.2-1
- initial package for Fedora