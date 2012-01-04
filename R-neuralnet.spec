%global packname  neuralnet
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.31
Release:          1%{?dist}
Summary:          Training of neural networks

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-grid R-MASS 

BuildRequires:    R-devel tex(latex) R-grid R-MASS 

%description
Training of neural networks using backpropagation, resilient
backpropagation with (Riedmiller, 1994) or without weight backtracking
(Riedmiller and Braun, 1993) or the modified globally convergent version
by Anastasiadis et al. (2005). The package allows flexible settings
through custom-choice of error and activation function. Furthermore, the
calculation of generalized weights (Intrator O & Intrator N, 1993) is

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
%doc %{rlibdir}/neuralnet/html
%doc %{rlibdir}/neuralnet/DESCRIPTION
%{rlibdir}/neuralnet/help
%{rlibdir}/neuralnet/Meta
%{rlibdir}/neuralnet/NAMESPACE
%{rlibdir}/neuralnet/INDEX
%{rlibdir}/neuralnet/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.31-1
- initial package for Fedora