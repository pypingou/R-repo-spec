%global packname  QCAGUI
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.7
Release:          1%{?dist}
Summary:          QCA Graphical User Interface

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk R-grDevices R-utils R-QCA R-MASS 


BuildRequires:    R-devel tex(latex) R-tcltk R-grDevices R-utils R-QCA R-MASS



%description
QCAGUI is a graphical user interface (GUI) for the QCA package, derived
from R Commander. Because QCA has little to do with statistics, the menus
from Rcmdr were stripped down to the very basics. In crisp sets QCA, data
is binary therefore it is fairly decent to treat it as categorical (1 -
presence; 0 - absence). In order to ease the primary analysis (e.g. tables
of frequencies) and the creation of basic graphs, this package activates
some menus that are not available in Rcmdr but for factors. Users should
be aware, however, that QCAGUI is not a package for statistics; Rcmdr is
better for this purpose

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.7-1
- initial package for Fedora