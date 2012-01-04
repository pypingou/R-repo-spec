%global packname  regsubseq
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.10
Release:          1%{?dist}
Summary:          Detect and Test Regular Sequences and Subsequences

Group:            Applications/Engineering 
License:          GPL 2.
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
For a sequence of event occurence times, we are interested in finding
subsequences in it that are too "regular". We define regular as being
significantly different from a homogeneous Poisson process. The departure
from the Poisson process is measured using a L1 distance. See Di and
Perlman 2007 for more details.

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
%doc %{rlibdir}/regsubseq/DESCRIPTION
%doc %{rlibdir}/regsubseq/html
%{rlibdir}/regsubseq/help
%{rlibdir}/regsubseq/NAMESPACE
%{rlibdir}/regsubseq/R
%{rlibdir}/regsubseq/INDEX
%{rlibdir}/regsubseq/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.10-1
- initial package for Fedora