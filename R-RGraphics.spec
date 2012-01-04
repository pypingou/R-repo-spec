%global packname  RGraphics
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Data and Functions from the book R Graphics, Second Edition

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-datasets R-stats R-grDevices R-graphics R-methods R-grid R-lattice R-ggplot2 

BuildRequires:    R-devel tex(latex) R-datasets R-stats R-grDevices R-graphics R-methods R-grid R-lattice R-ggplot2 

%description
Data and Functions from the book R Graphics, Second Edition. There is a
function to produce each figure in the book, plus several functions,
classes, and methods defined in Chapter 8.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.0-1
- initial package for Fedora