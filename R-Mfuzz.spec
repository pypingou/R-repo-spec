%global packname  Mfuzz
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.12.0
Release:          1%{?dist}
Summary:          Soft clustering of time series gene expression data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-e1071 
Requires:         R-tcltk R-tkWidgets 

BuildRequires:    R-devel tex(latex) R-Biobase R-e1071
BuildRequires:    R-tcltk R-tkWidgets 


%description
Package for noise-robust soft clustering of gene expression time-series
data (including a graphical user interface)

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
%doc %{rlibdir}/Mfuzz/doc
%doc %{rlibdir}/Mfuzz/html
%doc %{rlibdir}/Mfuzz/DESCRIPTION
%{rlibdir}/Mfuzz/data
%{rlibdir}/Mfuzz/Meta
%{rlibdir}/Mfuzz/NAMESPACE
%{rlibdir}/Mfuzz/R
%{rlibdir}/Mfuzz/help
%{rlibdir}/Mfuzz/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.12.0-1
- initial package for Fedora