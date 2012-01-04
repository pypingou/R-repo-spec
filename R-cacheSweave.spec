%global packname  cacheSweave
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6
Release:          1%{?dist}
Summary:          Tools for caching Sweave computations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-filehash R-stashR 
Requires:         R-utils R-digest 

BuildRequires:    R-devel tex(latex) R-filehash R-stashR
BuildRequires:    R-utils R-digest 


%description
Tools for caching Sweave computations and storing them in key-value

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
%doc %{rlibdir}/cacheSweave/DESCRIPTION
%doc %{rlibdir}/cacheSweave/COPYING
%doc %{rlibdir}/cacheSweave/html
%doc %{rlibdir}/cacheSweave/doc
%{rlibdir}/cacheSweave/example
%{rlibdir}/cacheSweave/NAMESPACE
%{rlibdir}/cacheSweave/R
%{rlibdir}/cacheSweave/Meta
%{rlibdir}/cacheSweave/misc
RPM build errors:
%{rlibdir}/cacheSweave/INDEX
%{rlibdir}/cacheSweave/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6-1
- initial package for Fedora