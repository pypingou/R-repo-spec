%global packname  minet
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.8.0
Release:          1%{?dist}
Summary:          Mutual Information NETworks

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-infotheo 

BuildRequires:    R-devel tex(latex) R-infotheo 

%description
This package implements various algorithms for inferring mutual
information networks from data.

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
%doc %{rlibdir}/minet/html
%doc %{rlibdir}/minet/CITATION
%doc %{rlibdir}/minet/DESCRIPTION
%{rlibdir}/minet/help
%{rlibdir}/minet/R
%{rlibdir}/minet/INDEX
%{rlibdir}/minet/LICENSE
%{rlibdir}/minet/NAMESPACE
%{rlibdir}/minet/libs
%{rlibdir}/minet/data
%{rlibdir}/minet/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.8.0-1
- initial package for Fedora