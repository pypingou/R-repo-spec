%global packname  playwith
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.53
Release:          1%{?dist}
Summary:          A GUI for interactive plots using GTK+

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-53.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-cairoDevice R-gWidgetsRGtk2 R-grid 
Requires:         R-RGtk2 R-gWidgets R-gridBase R-grDevices R-graphics R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-lattice R-cairoDevice R-gWidgetsRGtk2 R-grid
BuildRequires:    R-RGtk2 R-gWidgets R-gridBase R-grDevices R-graphics R-stats R-utils 


%description
A GTK+ graphical user interface for editing and interacting with R plots.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.53-1
- initial package for Fedora