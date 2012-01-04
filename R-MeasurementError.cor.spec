%global packname  MeasurementError.cor
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.26.0
Release:          1%{?dist}
Summary:          Measurement Error model estimate for correlation coefficient

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Two-stage measurement error model for correlation estimation with smaller
bias than the usual sample correlation

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
%doc %{rlibdir}/MeasurementError.cor/doc
%doc %{rlibdir}/MeasurementError.cor/DESCRIPTION
%doc %{rlibdir}/MeasurementError.cor/html
%{rlibdir}/MeasurementError.cor/Meta
%{rlibdir}/MeasurementError.cor/INDEX
%{rlibdir}/MeasurementError.cor/R
%{rlibdir}/MeasurementError.cor/NAMESPACE
%{rlibdir}/MeasurementError.cor/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.26.0-1
- initial package for Fedora