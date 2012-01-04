%global packname  SRPM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          Shared Reproducibility Package Management

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stashR 
Requires:         R-utils R-filehash R-cacheSweave R-stashR 

BuildRequires:    R-devel tex(latex) R-methods R-stashR
BuildRequires:    R-utils R-filehash R-cacheSweave R-stashR 


%description
A package development and management system for distributed reproducible

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
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.6-1
- initial package for Fedora