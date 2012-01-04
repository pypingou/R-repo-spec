%global packname  ROCwoGS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Non-parametric estimation of ROC curves without Gold Standard Test

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Function to estimate the ROC Curve of a continuous-scaled diagnostic test
with the help of a second imperfect diagnostic test with binary responses.

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
%doc %{rlibdir}/ROCwoGS/html
%doc %{rlibdir}/ROCwoGS/DESCRIPTION
%{rlibdir}/ROCwoGS/help
%{rlibdir}/ROCwoGS/data
%{rlibdir}/ROCwoGS/NAMESPACE
%{rlibdir}/ROCwoGS/Meta
%{rlibdir}/ROCwoGS/INDEX
%{rlibdir}/ROCwoGS/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora