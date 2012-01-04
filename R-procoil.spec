%global packname  procoil
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Prediction of Oligomerization of Coiled Coil Proteins

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
The procoil package allows to predict whether a coiled coil sequence
(amino acid sequence plus heptad register) is more likely to form a dimer
or more likely to form a trimer. The predict function not only computes
the prediction itself, but also a profile which allows to determine the
strengths to which the individual residues are indicative for either
class. Profiles can also be plotted and exported to files.

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
%doc %{rlibdir}/procoil/CITATION
%doc %{rlibdir}/procoil/DESCRIPTION
%doc %{rlibdir}/procoil/doc
%doc %{rlibdir}/procoil/html
%doc %{rlibdir}/procoil/NEWS
%{rlibdir}/procoil/help
%{rlibdir}/procoil/Meta
%{rlibdir}/procoil/data
%{rlibdir}/procoil/INDEX
%{rlibdir}/procoil/R
%{rlibdir}/procoil/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora