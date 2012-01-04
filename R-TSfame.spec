%global packname  TSfame
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2011.11.1
Release:          1%{?dist}
Summary:          Time Series Database Interface extensions for fame

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.11-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-tframe R-tframePlus R-TSdbi R-DBI R-fame R-tis R-zoo 
Requires:         R-methods R-DBI R-TSdbi R-tframe 

BuildRequires:    R-devel tex(latex) R-methods R-tframe R-tframePlus R-TSdbi R-DBI R-fame R-tis R-zoo
BuildRequires:    R-methods R-DBI R-TSdbi R-tframe 


%description
TSfame provides a fame interface for TSdbi.

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
%doc %{rlibdir}/TSfame/NEWS
%doc %{rlibdir}/TSfame/html
%doc %{rlibdir}/TSfame/DESCRIPTION
%doc %{rlibdir}/TSfame/doc
%{rlibdir}/TSfame/LICENSE
%{rlibdir}/TSfame/INDEX
%{rlibdir}/TSfame/help
%{rlibdir}/TSfame/Meta
%{rlibdir}/TSfame/NAMESPACE
%{rlibdir}/TSfame/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.11.1-1
- initial package for Fedora