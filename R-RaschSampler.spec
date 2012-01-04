%global packname  RaschSampler
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.5
Release:          1%{?dist}
Summary:          Rasch Sampler

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Sampling binary matrices with fixed margins

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
%doc %{rlibdir}/RaschSampler/html
%doc %{rlibdir}/RaschSampler/DESCRIPTION
%{rlibdir}/RaschSampler/data
%{rlibdir}/RaschSampler/NAMESPACE
%{rlibdir}/RaschSampler/libs
%{rlibdir}/RaschSampler/R
%{rlibdir}/RaschSampler/help
%{rlibdir}/RaschSampler/Meta
%{rlibdir}/RaschSampler/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.5-1
- initial package for Fedora