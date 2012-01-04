%global packname  MSeasyTkGUI
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          5.2
Release:          1%{?dist}
Summary:          MSeasy Tcl/Tk Graphical User Interface

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MSeasy R-tcltk 

BuildRequires:    R-devel tex(latex) R-MSeasy R-tcltk 

%description
A Tcl/Tk GUI for some basic functions in the MSeasy package

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 5.2-1
- initial package for Fedora