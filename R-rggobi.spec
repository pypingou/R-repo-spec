%global packname  rggobi
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.17
Release:          1%{?dist}
Summary:          Interface between R and GGobi

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-RGtk2 R-utils R-methods 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-RGtk2 R-utils R-methods 


%description
The rggobi package provides a command-line interface to GGobi, an
interactive and dynamic graphics package. Rggobi complements GGobi's
graphical user interface, providing a way to fluidly transition between
analysis and exploration, as well as automating common tasks.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.17-1
- initial package for Fedora