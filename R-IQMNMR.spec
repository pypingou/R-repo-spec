%global packname  IQMNMR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Identification and Quantification of Metabolites by Using 1D 1H NMR FID

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-neldermead R-Rmpi R-papply R-signal R-outliers 


BuildRequires:    R-devel tex(latex) R-neldermead R-Rmpi R-papply R-signal R-outliers



%description
Critical to metabolomics is the unambiguous identification and absolute
quantification of metabolites. One-dimensional (1D) proton (1H) NMR has
formed the bedrock of metabolomics studies to date. Automated and high
throughput identification and quantification of metabolites is a big
challenge for One-dimensional (1D) proton (1H) NMR. This package present a
new automated technique based on Message Passing Interface (MPI),
relaxation algorithm, pattern identification, Madison Metabolomics
Consortium Database (MMCD), and 1D 1H NMR free induction decay (FID), for
the unambiguous identification and absolute quantification of targeted

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
%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.7-1
- initial package for Fedora