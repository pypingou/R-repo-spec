%global packname  dismo
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.11
Release:          1%{?dist}
Summary:          Species distribution modeling

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-raster R-sp 

BuildRequires:    R-devel tex(latex) R-methods R-raster R-sp 

%description
Functions for species distribution modeling, that is, predicting entire
geographic distributions form occurences at specific sites.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.11-1
- initial package for Fedora