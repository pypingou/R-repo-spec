%global packname  joda
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          JODA algorithm for quantifying gene deregulation using knowledge

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-bgmm R-RBGL 

BuildRequires:    R-devel tex(latex) R-bgmm R-RBGL 

%description
Package 'joda' implements three steps of an algorithm called JODA. The
algorithm computes gene deregulation scores. For each gene, its
deregulation score reflects how strongly an effect of a certain
regulator's perturbation on this gene differs between two different cell
populations. The algorithm utilizes regulator knockdown expression data as
well as knowledge about signaling pathways in which the regulators are
involved (formalized in a simple matrix model).

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
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora