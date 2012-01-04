%global packname  sizepower
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.24.0
Release:          1%{?dist}
Summary:          Sample Size and Power Calculation in Micorarray Studies

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
This package has been prepared to assist users in computing either a
sample size or power value for a microarray experimental study. The user
is referred to the cited references for technical background on the
methodology underpinning these calculations. This package provides support
for five types of sample size and power calculations. These five types can
be adapted in various ways to encompass many of the standard designs
encountered in practice.

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
%doc %{rlibdir}/sizepower/html
%doc %{rlibdir}/sizepower/DESCRIPTION
%doc %{rlibdir}/sizepower/doc
%{rlibdir}/sizepower/NAMESPACE
%{rlibdir}/sizepower/INDEX
%{rlibdir}/sizepower/R
%{rlibdir}/sizepower/help
%{rlibdir}/sizepower/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.24.0-1
- initial package for Fedora