%global packname  RgoogleMaps
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.9.15
Release:          1%{?dist}
Summary:          Overlays on Google map tiles in R

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-stats R-utils R-png 

BuildRequires:    R-devel tex(latex) R-graphics R-stats R-utils R-png 

%description
This package serves two purposes: (i) Provide a comfortable R interface to
query the Google server for static maps, and (ii) Use the map as a
background image to overlay plots within R. This requires proper
coordinate scaling. NOTE: To do anything but downloading static map tiles,
RgoogleMaps needs EITHER png OR ReadImages OR rimage installed ! png
(default) is your package if you prefer png file format and ReadImages or
rimage if you prefer jpg format. In the latter cases, you will also need
the libjpeg library installed.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.9.15-1
- initial package for Fedora