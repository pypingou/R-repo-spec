%global packname  trip
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.10
Release:          1%{?dist}
Summary:          Spatial analysis of animal track data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-sp R-spatstat 

BuildRequires:    R-devel tex(latex) R-methods R-sp R-spatstat 

%description
Functions for accessing and manipulating spatial data for animal tracking.
Filter for speed and create time spent plots from animal track data.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.10-1
- initial package for Fedora