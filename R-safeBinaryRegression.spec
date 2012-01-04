%global packname  safeBinaryRegression
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Safe Binary Regression

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lpSolveAPI 


BuildRequires:    R-devel tex(latex) R-lpSolveAPI



%description
Overloads the glm function in the stats package so that a test for the
existence of the maximum likelihood estimate is included in the fitting
procedure for binary regression models.

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
%doc %{rlibdir}/safeBinaryRegression/DESCRIPTION
%doc %{rlibdir}/safeBinaryRegression/html
%{rlibdir}/safeBinaryRegression/R
%{rlibdir}/safeBinaryRegression/NAMESPACE
%{rlibdir}/safeBinaryRegression/help
%{rlibdir}/safeBinaryRegression/INDEX
%{rlibdir}/safeBinaryRegression/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora