%global packname  fts
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.6
Release:          1%{?dist}
Summary:          R interface to tslib (a time series library in c++)

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils R-stats 

BuildRequires:    R-devel tex(latex) R-utils R-stats 

%description
fast operations for time series objects

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
%doc %{rlibdir}/fts/DESCRIPTION
%doc %{rlibdir}/fts/html
%{rlibdir}/fts/NAMESPACE
%{rlibdir}/fts/INDEX
%{rlibdir}/fts/R
%{rlibdir}/fts/help
%{rlibdir}/fts/libs
%{rlibdir}/fts/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.6-1
- initial package for Fedora