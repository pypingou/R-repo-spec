%global packname  gpairs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          gpairs: The Generalized Pairs Plot

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-barcode R-grid R-lattice R-vcd R-MASS R-colorspace 

BuildRequires:    R-devel tex(latex) R-barcode R-grid R-lattice R-vcd R-MASS R-colorspace 

%description
Produces a generalized pairs (gpairs) plot.

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
%doc %{rlibdir}/gpairs/html
%doc %{rlibdir}/gpairs/DESCRIPTION
%{rlibdir}/gpairs/INDEX
%{rlibdir}/gpairs/R
%{rlibdir}/gpairs/Meta
%{rlibdir}/gpairs/help
%{rlibdir}/gpairs/data

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora