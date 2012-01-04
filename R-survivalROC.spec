%global packname  survivalROC
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Time-dependent ROC curve estimation from censored survival data

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Compute time-dependent ROC curve from censored survival data using
Kaplan-Meier (KM) or Nearest Neighbor Estimation (NNE)  method of 
Heagerty, Lumley & Pepe (Biometrics, Vol 56 No 2, 2000, PP 337-344)

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
%doc %{rlibdir}/survivalROC/html
%doc %{rlibdir}/survivalROC/DESCRIPTION
%{rlibdir}/survivalROC/libs
%{rlibdir}/survivalROC/R
%{rlibdir}/survivalROC/NAMESPACE
%{rlibdir}/survivalROC/help
%{rlibdir}/survivalROC/data
%{rlibdir}/survivalROC/INDEX
%{rlibdir}/survivalROC/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora