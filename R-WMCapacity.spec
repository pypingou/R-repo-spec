%global packname  WMCapacity
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.6.6
Release:          1%{?dist}
Summary:          GUI implementing Bayesian working memory models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-gtools R-gWidgets R-gWidgetsRGtk2 R-coda R-cairoDevice 
Requires:         R-RGtk2 R-grDevices R-XML 

BuildRequires:    R-devel tex(latex) R-gtools R-gWidgets R-gWidgetsRGtk2 R-coda R-cairoDevice
BuildRequires:    R-RGtk2 R-grDevices R-XML 


%description
A GUI R implementation of hierarchical Bayesian models of working memory,
used for analyzing change detection data.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.6.6-1
- initial package for Fedora