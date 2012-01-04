%global packname  rmac
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9
Release:          1%{?dist}
Summary:          calculate RMAC or FMAC agreement coefficients

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-boot 

BuildRequires:    R-devel tex(latex) R-boot 

%description
Calculate Cohen's kappa, Scott's Pi, or the RMAC concordance correlation

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
%doc %{rlibdir}/rmac/DESCRIPTION
%doc %{rlibdir}/rmac/doc
%doc %{rlibdir}/rmac/CITATION
%doc %{rlibdir}/rmac/html
%{rlibdir}/rmac/R
%{rlibdir}/rmac/NAMESPACE
%{rlibdir}/rmac/help
%{rlibdir}/rmac/INDEX
%{rlibdir}/rmac/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9-1
- initial package for Fedora