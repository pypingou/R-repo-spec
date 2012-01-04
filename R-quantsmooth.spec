%global packname  quantsmooth
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.20.0
Release:          1%{?dist}
Summary:          Quantile smoothing and genomic visualization of array data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-quantreg R-lodplot R-grid 


BuildRequires:    R-devel tex(latex) R-quantreg R-lodplot R-grid



%description
Implements quantile smoothing as introduced in: Quantile smoothing of
array CGH data; Eilers PH, de Menezes RX; Bioinformatics. 2005 Apr

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
%doc %{rlibdir}/quantsmooth/html
%doc %{rlibdir}/quantsmooth/doc
%doc %{rlibdir}/quantsmooth/DESCRIPTION
%{rlibdir}/quantsmooth/Meta
%{rlibdir}/quantsmooth/NAMESPACE
%{rlibdir}/quantsmooth/R
%{rlibdir}/quantsmooth/help
%{rlibdir}/quantsmooth/data
%{rlibdir}/quantsmooth/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.20.0-1
- initial package for Fedora