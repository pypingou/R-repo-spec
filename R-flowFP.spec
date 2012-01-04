%global packname  flowFP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12.1
Release:          1%{?dist}
Summary:          Fingerprinting for Flow Cytometry

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-flowCore R-flowViz 

BuildRequires:    R-devel tex(latex) R-flowCore R-flowViz 

%description
Fingerprint generation of flow cytometry data, used to facilitate the
application of machine learning and datamining tools for flow cytometry.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.1-1
- initial package for Fedora