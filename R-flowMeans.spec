%global packname  flowMeans
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Non-parametric Flow Cytometry Data Gating

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-Biobase R-graphics R-grDevices R-methods R-rrcov R-stats R-feature R-flowCore 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Biobase R-graphics R-grDevices R-methods R-rrcov R-stats R-feature R-flowCore 


%description
Identifies cell populations in Flow Cytometry data using non-parametric
clustering and segmented-regression-based change point detection. Note: R
2.11.0 or newer is required.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora