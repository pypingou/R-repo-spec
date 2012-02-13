%global packname  reporttools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.7
Release:          1%{dist}
Summary:          Generate LaTeX tables of descriptive statistics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-xtable 

BuildRequires:    R-devel tex(latex) R-xtable 

%description
The functions in this package are especially helpful when writing reports
of data analysis using Sweave.

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
%doc %{rlibdir}/reporttools/html
%doc %{rlibdir}/reporttools/doc
%doc %{rlibdir}/reporttools/NEWS
%doc %{rlibdir}/reporttools/CITATION
%doc %{rlibdir}/reporttools/DESCRIPTION
%{rlibdir}/reporttools/help
%{rlibdir}/reporttools/Meta
%{rlibdir}/reporttools/R
%{rlibdir}/reporttools/INDEX
%{rlibdir}/reporttools/NAMESPACE

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.7-1
- Update to version 1.0.7

* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.6-1
- initial package for Fedora