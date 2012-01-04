%global packname  dks
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          The double Kolmogorov-Smirnov package for evaluating multiple testing procedures.

Group:            Applications/Engineering 
License:          GPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-cubature 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-cubature 


%description
The dks package consists of a set of diagnostic functions for multiple
testing methods. The functions can be used to determine if the p-values
produced by a multiple testing procedure are correct. These functions are
designed to be applied to simulated data. The functions require the entire
set of p-values from multiple simulated studies, so that the joint
distribution can be evaluated.

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
%doc %{rlibdir}/dks/NEWS
%doc %{rlibdir}/dks/DESCRIPTION
%doc %{rlibdir}/dks/doc
%doc %{rlibdir}/dks/html
%{rlibdir}/dks/data
%{rlibdir}/dks/NAMESPACE
%{rlibdir}/dks/INDEX
%{rlibdir}/dks/Meta
%{rlibdir}/dks/help
%{rlibdir}/dks/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora