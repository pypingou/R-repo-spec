%global packname  compOverlapCorr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Comparing overlapping correlation coefficients

Group:            Applications/Engineering 
License:          GPL version 2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains function to test the difference between two
overlapping (in the sense of having a variable in common) correlation
coefficients, using a Z-test as described by Meng, Rosenthal, and Rubin
(Meng et al, 1992).

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
%doc %{rlibdir}/compOverlapCorr/html
%doc %{rlibdir}/compOverlapCorr/DESCRIPTION
%{rlibdir}/compOverlapCorr/help
%{rlibdir}/compOverlapCorr/R
%{rlibdir}/compOverlapCorr/NAMESPACE
%{rlibdir}/compOverlapCorr/INDEX
%{rlibdir}/compOverlapCorr/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora