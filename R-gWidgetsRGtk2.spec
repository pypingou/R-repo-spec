%global packname  gWidgetsRGtk2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.77
Release:          1%{?dist}
Summary:          Toolkit implementation of gWidgets for RGtk2

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-77.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-gWidgets 
Requires:         R-RGtk2 

BuildRequires:    R-devel tex(latex) R-methods R-gWidgets
BuildRequires:    R-RGtk2 


%description
Port of gWidgets API to RGtk2

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.77-1
- initial package for Fedora