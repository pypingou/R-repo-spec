%global packname  PLIS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Multiplicity control using Pooled LIS statisitcs

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
PLIS is a multiple testing procedure for testing several groups of
hypotheses. Linear dependency is expected from the hypotheses within the
same group and is modeled by hidden Markov Models. It is noted that, for
PLIS, a smaller p value does not necessarily imply more significance
because of dependency among the hypotheses. A typical applicaiton of PLIS
is to analyze genome wide association studies datasets, where SNPs from
the same chromosome are treated as a group and exhibit strong linear
genomic dependency.

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
%doc %{rlibdir}/PLIS/DESCRIPTION
%doc %{rlibdir}/PLIS/html
%{rlibdir}/PLIS/INDEX
%{rlibdir}/PLIS/data
%{rlibdir}/PLIS/R
%{rlibdir}/PLIS/NAMESPACE
%{rlibdir}/PLIS/Meta
%{rlibdir}/PLIS/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora