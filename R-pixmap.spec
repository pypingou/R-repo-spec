%global packname  pixmap
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4.11
Release:          1%{?dist}
Summary:          Bitmap Images (``Pixel Maps'')

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Functions for import, export, plotting and other manipulations of
bitmapped images.

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
%doc %{rlibdir}/pixmap/DESCRIPTION
%doc %{rlibdir}/pixmap/html
%doc %{rlibdir}/pixmap/NEWS
%{rlibdir}/pixmap/INDEX
%{rlibdir}/pixmap/NAMESPACE
%{rlibdir}/pixmap/Meta
%{rlibdir}/pixmap/pictures
%{rlibdir}/pixmap/R
%{rlibdir}/pixmap/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.11-1
- initial package for Fedora