%global packname  IBDsim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8
Release:          1%{?dist}
Summary:          Simulation of chromosomal regions shared by family members.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-paramlink 


BuildRequires:    R-devel tex(latex) R-paramlink



%description
R package for simulation of IBD sharing among family members. Using sex
specific recombination rates from the Decode map (2010) of the human
genome, phased chromosomes are simulated for all pedigree members, either
by unconditional 'gene dropping' or conditional on a specified IBD
pattern. Regions compatible with the query IBD pattern (possibly different
from the conditional pattern) are subsequently detected and summarized.

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
%doc %{rlibdir}/IBDsim/html
%doc %{rlibdir}/IBDsim/DESCRIPTION
%{rlibdir}/IBDsim/libs
%{rlibdir}/IBDsim/Meta
%{rlibdir}/IBDsim/help
%{rlibdir}/IBDsim/INDEX
%{rlibdir}/IBDsim/data
%{rlibdir}/IBDsim/R
%{rlibdir}/IBDsim/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8-1
- initial package for Fedora