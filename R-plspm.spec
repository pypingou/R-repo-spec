%global packname  plspm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.11
Release:          1%{?dist}
Summary:          Partial Least Squares Data Analysis Methods

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-amap R-diagram 

BuildRequires:    R-devel tex(latex) R-amap R-diagram 

%description
Partial Least Squares (PLS) methods with emphasis on structural equation
models with latent variables.

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
%doc %{rlibdir}/plspm/html
%doc %{rlibdir}/plspm/DESCRIPTION
%{rlibdir}/plspm/R
%{rlibdir}/plspm/data
%{rlibdir}/plspm/help
%{rlibdir}/plspm/INDEX
%{rlibdir}/plspm/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.11-1
- initial package for Fedora