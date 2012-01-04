%global packname  NTW
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Predict gene network using an Ordinary Differential Equation (ODE) based method

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-mvtnorm R-stats R-utils 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-mvtnorm R-stats R-utils 


%description
This package predicts the gene-gene interaction network and identifies the
direct transcriptional targets of the perturbation using an ODE (Ordinary
Differential Equation) based method.

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
%doc %{rlibdir}/NTW/NEWS
%doc %{rlibdir}/NTW/html
%doc %{rlibdir}/NTW/DESCRIPTION
%doc %{rlibdir}/NTW/doc
%{rlibdir}/NTW/NAMESPACE
%{rlibdir}/NTW/data
%{rlibdir}/NTW/INDEX
%{rlibdir}/NTW/help
%{rlibdir}/NTW/Meta
%{rlibdir}/NTW/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora