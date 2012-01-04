%global packname  DCluster
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.3
Release:          1%{?dist}
Summary:          Functions for the detection of spatial clusters of diseases

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-boot R-spdep 


BuildRequires:    R-devel tex(latex) R-boot R-spdep



%description
A set of functions for the detection of spatial clusters of disease using
count data. Bootstrap is used to estimate sampling distributions of

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.3-1
- initial package for Fedora