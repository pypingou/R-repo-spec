%global packname  formatR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.4
Release:          1%{?dist}
Summary:          Format R Code Automatically

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-parser 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-parser 


%description
This package provides a function tidy.source() and optionally a GUI (by
gWidgets and preferably gWidgetsRGtk2) to format R source code.  Spaces
and indent will be added to the code automatically, and comments will be
preserved under certain conditions, so that R code will be more
human-readable and tidy.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.4-1
- initial package for Fedora