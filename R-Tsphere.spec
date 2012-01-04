%global packname  Tsphere
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Transposable Sphering for Large-Scale Inference with Correlated Data.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-glasso R-rms 


BuildRequires:    R-devel tex(latex) R-glasso R-rms



%description
Adjusts for correlations among the rows and columns via the Transposable
Sphering Algorithm when conducting large-scale inference on the rows of a
data matrix.

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
%doc %{rlibdir}/Tsphere/html
%doc %{rlibdir}/Tsphere/DESCRIPTION
%{rlibdir}/Tsphere/help
%{rlibdir}/Tsphere/Meta
%{rlibdir}/Tsphere/R
%{rlibdir}/Tsphere/INDEX
%{rlibdir}/Tsphere/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora