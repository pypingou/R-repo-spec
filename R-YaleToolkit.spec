%global packname  YaleToolkit
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.2
Release:          1%{?dist}
Summary:          Data exploration tools from Yale University.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-grid R-lattice R-vcd R-MASS R-colorspace 

BuildRequires:    R-devel tex(latex) R-grid R-lattice R-vcd R-MASS R-colorspace 

%description
This collection of data exploration tools was developed at Yale University
for the graphical exploration of complex multivariate data. Functions
provided include \code{barcode()}, \code{gpairs()}, \code{corrgram()},
\code{whatis()}, \code{sparkline()}, \code{sparklines()}, and

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
%doc %{rlibdir}/YaleToolkit/DESCRIPTION
%doc %{rlibdir}/YaleToolkit/html
%{rlibdir}/YaleToolkit/help
%{rlibdir}/YaleToolkit/data
%{rlibdir}/YaleToolkit/Meta
%{rlibdir}/YaleToolkit/R
%{rlibdir}/YaleToolkit/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.2-1
- initial package for Fedora