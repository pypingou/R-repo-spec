%global packname  plier
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.24.0
Release:          1%{?dist}
Summary:          Implements the Affymetrix PLIER algorithm

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 
Requires:         R-affy R-Biobase R-methods 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-affy R-Biobase R-methods 


%description
The PLIER (Probe Logarithmic Error Intensity Estimate) method produces an
improved signal by accounting for experimentally observed patterns in
probe behavior and handling error at the appropriately at low and high
signal values.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.24.0-1
- initial package for Fedora