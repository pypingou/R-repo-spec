%global packname  emplik
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.7
Release:          1%{?dist}
Summary:          Empirical likelihood ratio for censored/truncated data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-quantreg 


BuildRequires:    R-devel tex(latex) R-quantreg



%description
empirical likelihood ratio tests for means/quantiles/hazards from possibly
censored and/or truncated data. Now does regression too.

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
%doc %{rlibdir}/emplik/html
%doc %{rlibdir}/emplik/doc
%doc %{rlibdir}/emplik/DESCRIPTION
%{rlibdir}/emplik/INDEX
%{rlibdir}/emplik/help
%{rlibdir}/emplik/Meta
%{rlibdir}/emplik/data
%{rlibdir}/emplik/NAMESPACE
%{rlibdir}/emplik/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.7-1
- initial package for Fedora