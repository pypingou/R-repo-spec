%global packname  relaxo
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Relaxed Lasso

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lars 

BuildRequires:    R-devel tex(latex) R-lars 

%description
Relaxed Lasso is a generalisation of the Lasso shrinkage technique for
linear regression. Both variable selection and parameter estimation is
achieved by regular Lasso, yet both steps do not necessarily use the same
penalty parameter. The results include all standard Lasso solutions but
allow often for sparser models while having similar or even slightly
better predictive performance if many predictor variables are present. The
package depends on the LARS package.

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
%doc %{rlibdir}/relaxo/DESCRIPTION
%doc %{rlibdir}/relaxo/html
%{rlibdir}/relaxo/INDEX
%{rlibdir}/relaxo/NAMESPACE
%{rlibdir}/relaxo/help
%{rlibdir}/relaxo/R
%{rlibdir}/relaxo/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora