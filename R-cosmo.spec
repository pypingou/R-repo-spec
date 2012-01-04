%global packname  cosmo
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.20.0
Release:          1%{?dist}
Summary:          Supervised detection of conserved motifs in DNA sequences

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-utils R-seqLogo 

BuildRequires:    R-devel tex(latex) R-methods R-utils R-seqLogo 

%description
cosmo searches a set of unaligned DNA sequences for a shared motif that
may, for example, represent a common transcription factor binding site.
The algorithm is similar to MEME, but also allows the user to specify a
set of constraints that the position weight matrix of the unknown motif
must satisfy. Such constraints may include bounds on the information
content across certain regions of the unknown motif, for example, and can
often be formulated on the basis of prior knowledge about the structure of
the transcription factor in question. The unknown motif width, the
distribution of motif occurrences (OOPS, ZOOPS, or TCM), as well as the
appropriate constraint set can be selected data-adaptively.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.20.0-1
- initial package for Fedora