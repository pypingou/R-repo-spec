%global packname  cellVolumeDist
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Functions to fit cell volume distributions and thereby estimate cell growth rates and division times

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-minpack.lm R-gplots 

BuildRequires:    R-devel tex(latex) R-minpack.lm R-gplots 

%description
This package implements a methodology for using cell volume distributions
to estimate cell growth rates and division times that is described in the
paper entitled "Cell Volume Distributions Reveal Cell Growth Rates and
Division Times", by Michael Halter, John T. Elliott, Joseph B. Hubbard,
Alessandro Tona and Anne L. Plant, which is in press in the Journal of
Theoretical Biology.  In order to reproduce the analysis used to obtain
Table 1 in the paper, execute the command "example(fitVolDist)".

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora