%global packname  Epi
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.33
Release:          1%{dist}
Summary:          A package for statistical analysis in epidemiology.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
Functions for demographic and epidemiological analysis in the Lexis
diagram, i.e. register and cohort follow-up data, including interval
censored data and representation of multistate data. Also some useful
functions for tabulation and plotting. Contains some epidemiological

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
%doc %{rlibdir}/Epi/CITATION
%doc %{rlibdir}/Epi/DESCRIPTION
%doc %{rlibdir}/Epi/doc
%doc %{rlibdir}/Epi/html
%{rlibdir}/Epi/libs
%{rlibdir}/Epi/help
%{rlibdir}/Epi/Meta
%{rlibdir}/Epi/data
%{rlibdir}/Epi/INDEX
%{rlibdir}/Epi/R
%{rlibdir}/Epi/NAMESPACE

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.33-1
- Update to version 1.1.33

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.24-1
- initial package for Fedora