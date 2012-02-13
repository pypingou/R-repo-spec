%global packname  fast
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.60
Release:          1%{dist}
Summary:          Implementation of the Fourier Amplitute Sensitivity Test (FAST)

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The Fourier Amplitute Sensitivity Test (FAST) is a method to deterimine
global sensitivities of a model on parameter changes with relavtively few
model runs. This package implements this sensitivity analysis method.

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
%doc %{rlibdir}/fast/DESCRIPTION
%doc %{rlibdir}/fast/html
%{rlibdir}/fast/R
%{rlibdir}/fast/NAMESPACE
%{rlibdir}/fast/help
%{rlibdir}/fast/INDEX
%{rlibdir}/fast/Meta

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.60-1
- Update to version 0.60

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.51-1
- initial package for Fedora