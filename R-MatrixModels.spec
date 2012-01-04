%global packname  MatrixModels
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Modelling with Sparse And Dense Matrices

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-utils R-methods R-Matrix 

BuildRequires:    R-devel tex(latex) R-stats R-utils R-methods R-Matrix 

%description
Modelling with sparse and dense 'Matrix' matrices, using modular
prediction and response module classes.

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
%doc %{rlibdir}/MatrixModels/html
%doc %{rlibdir}/MatrixModels/DESCRIPTION
%{rlibdir}/MatrixModels/INDEX
%{rlibdir}/MatrixModels/R
%{rlibdir}/MatrixModels/NAMESPACE
%{rlibdir}/MatrixModels/help
%{rlibdir}/MatrixModels/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.1-1
- initial package for Fedora