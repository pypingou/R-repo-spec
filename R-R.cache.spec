%global packname  R.cache
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.2
Release:          1%{?dist}
Summary:          Fast and light-weight caching (memoization) of objects

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-R.methodsS3 R-R.oo R-R.utils 

BuildRequires:    R-devel tex(latex) R-R.methodsS3 R-R.oo R-R.utils 

%description
Methods for memoization, that is, caching arbitrary R objects in
persistent memory.  Objects can be loaded and saved stratified on a set of
hashing objects.

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
%doc %{rlibdir}/R.cache/NEWS
%doc %{rlibdir}/R.cache/html
%doc %{rlibdir}/R.cache/DESCRIPTION
%{rlibdir}/R.cache/R
%{rlibdir}/R.cache/NAMESPACE
%{rlibdir}/R.cache/help
%{rlibdir}/R.cache/INDEX
%{rlibdir}/R.cache/Meta

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.2-1
- initial package for Fedora